# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Read products": "/products/",
        "Create product(s)": "/products/",
        "Read product(s)": "/products/<str:pk>/",
        "Update product(s)": "/products/<str:pk>/",
        "Delete product(s)": "/products/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET", "POST"])
def products(request):
    if request.method == "POST":
        try: 
            if (
                request.data == {}
                or request.data["name"] == ""
                or request.data["description"] == ""
            ):
                return Response(
                    {"ok": "false", "message": "Product name and description are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"ok": "true", "message": "Created product!", "data": serializer.data},
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"ok": "false", "message": "Error creating product in the database!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except: 
            return Response(
                {"ok": "false", "message": "Something went wrong!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    if request.method == "GET":
        try:
            products = Product.objects.all().order_by("id")
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {"ok": "false", "message": "Something went wrong!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@api_view(["GET", "PUT", "DELETE"])
def productDetail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return Response("Resource successfully deleted!")

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
