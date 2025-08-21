from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny

from materials.models import Course
from .models import Payment, User
from .serializers import PaymentSerializer, UserSerializer
from rest_framework.generics import CreateAPIView

from .services import create_stripe_product, create_stripe_price, create_stripe_session


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        "paid_course": ["exact", "isnull"],
        "paid_lesson": ["exact", "isnull"],
        "payment_method": ["exact"],
        "payment_date": ["gte", "lte", "exact"],
        "amount": ["gte", "lte", "exact"],
    }
    ordering_fields = ["payment_date", "amount"]
    ordering = ["payment_date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.request.data.get('course'))
        description = Course.objects.get(description=self.request.data.get('description'))
        payment = serializer.save(user=self.request.user)
        amount = payment.amount
        product = create_stripe_product(course,description)
        price = create_stripe_price(amount, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
