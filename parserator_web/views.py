import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        try:
            parse_result = self.parse(request.query_params['address'])
        except usaddress.RepeatedLabelError:
            return Response({
                'error': 'This string could not be parsed.'
            }, status=500)
        return Response({
            'input_string': request.query_params['address'],
            'address_components': parse_result[0],
            'address_type': parse_result[1]
        })

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
