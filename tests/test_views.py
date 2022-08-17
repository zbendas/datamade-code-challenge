from django.urls import reverse
from django.utils.http import urlencode


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    url = reverse('address-parse')
    response = client.get(url + '?' + urlencode({'address': address_string}))
    assert response.status_code == 200
    assert response.content == b'{"input_string":"123 main st chicago il",' \
                               b'"address_components":{"AddressNumber":"123",' \
                               b'"StreetName":"main",' \
                               b'"StreetNamePostType":"st",' \
                               b'"PlaceName":"chicago","StateName":"il"},' \
                               b'"address_type":"Street Address"}'


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    response = client.get(url + '?' + urlencode({'address': address_string}))
    assert response.status_code == 500
    assert response.content == b'{"error":"This string could not be parsed."}'
