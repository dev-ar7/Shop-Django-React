from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from store.models import Product, Rating


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    def create_order(self, request):

        if request.method == 'POST':
            order = request.data.get('order')
            cart = request.data.get('order')['cart']
            rating = request.data.get('order')['rating']

            for item in cart:
                item.pop('image')
                item_id = item.get('itemId')
                item_qty = item.get('qty')
                prod = Product.objects.get(pk = item_id)

                if prod.inventory == 0:
                    return Response({'message': 'No Item Left',}, status=status.HTTP_409_CONFLICT)

                prod.inventory = prod.inventory - item_qty
                prod.save()
            
            if rating:
                for r in rating:
                    item_id = item.get('itemId')
                    value = item.get('value')
                    r = Rating.objects.get(product = item_id)
                    if value == 1:
                        r.one += 1
                    elif value == 2:
                        r.two += 1
                    elif value == 3:
                        r.three += 1
                    elif value == 4:
                        r.four += 1
                    elif value == 5:
                        r.five += 1
                    r.save()

            serializer = self.serializer_class(data=order,
                                               context = {
                                                   'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
