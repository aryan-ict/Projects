odoo.define('student_website_portal', function(require){
    "use strict";

    console.log(">>>>>>>>Js loaded<<<<<<<");
    var ajax = require('web.ajax');

    $(document).ready(function(){
//        var state = $("#state").val(response)
        $("#submit_btn").click(function(){
            var name = $("#name").val()
            var phone = $("#phone").val()
            var date = $("#birth_date").val()
            var email = $("#email").val()
            var teacher = $("#allocated_id").val()
            var address = $("#address_panel").text()
            var country = $("#country").val()
            var state = $("#state").val()
            var street = $("#street").val()
            var street2 = $("#street2").val()
            var city = $("#city").val()
            var zip = $("#zip").val()
                console.log(">>>>>>>>>>>It works");
                $("#allocated_id").toggle();
                ajax.jsonRpc('/thankyou', 'call', {
                    'name': name,
                    'phone': phone,
                    'birth_date': date,
                    'email': email,
                    'allocated_id': teacher,
                    'street': street,
                    'street2': street2,
                    'city': city,
                    'zip': zip,
                    'country_id': country,
                }).then(function(response){
                    console.log("state", state);
                    console.log(">>>>>>>>>>It worked", response);
                });
        });
    });
});
