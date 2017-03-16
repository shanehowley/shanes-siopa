/**
 * Created by shane on 16/03/2017.
 */
$(function () {
    $("#payment-form").submit(function () {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };


        Stripe.createToken(card, function (status, response) {
            if (status === 200) {
                console.log(status, response);
                $("#credit-card-errors").hide();
                $("#id_stripe_id").val(response.id);
                form.submit();
            } else {
                $("#stripe-error-message").text(response.error.message);
                $("#credit-card-errors").show();
                $("#validate_ca rd_btn").attr("disabled", false);
            }
        });
        return false;
    });
});
