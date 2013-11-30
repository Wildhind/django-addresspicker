$(function(){
    $('.addresspicker-widget').each(function(){
        var $widget = $(this),
            $latlng = $widget.find('.addresspicker-result'),
            $map = $widget.find('.addresspicker-map'),
            $searchField = $widget.find('.addresspicker-search'),
            lat = $widget.find('.addresspicker-initial-lat').val(),
            lng = $widget.find('.addresspicker-initial-lng').val(),
            addresspickerMap = $searchField.addresspicker({
                elements: {
                    map: $map,
                    latlng: $latlng
                },
                mapOptions: {
                    center: new google.maps.LatLng(lat, lng)
                }
            }),
            marker = addresspickerMap.addresspicker("marker")
        marker.setVisible(true)
        addresspickerMap.addresspicker("updatePosition")
    })
})
