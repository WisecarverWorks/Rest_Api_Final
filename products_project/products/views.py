from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    

    #if request.method == 'GET':

    #elif request == 'POST':
        #serializer = ProductSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response(serializer.data, status=status.HTTP_201_CREATED)

#@api_view(['GET','PUT','DELETE'])
#def product_detail(request, pk):
    #product = get_object_else_404(Product, pk = pk)
    #if request.method == 'GET':
        #serializer = ProductSerializer(product, )
        #return Response(serializer.data)

    #elif request.method == 'PUT':
        #serializer = ProductSerializer(product, pk = pk)
        #serializer.is_valid(raise_exception = True)
        #serializer.save()
        #return Response(serializer.data)
    #elif request.method == 'DELETE':
        #product.delete()
        #return Response(status = status.HTTP_204_NO_CONTENT)