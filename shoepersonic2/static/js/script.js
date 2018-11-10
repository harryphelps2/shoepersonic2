$(document).ready(function(){

	$(".minus, .plus").click(function(e){
		var $button = $(this);
		var $quantity = $button.siblings(".quantity");
		var quantity = parseInt($quantity.text());

		if ($button.hasClass("minus")){
			quantity--;
		} else {
			quantity++;
		}
			$quantity.text(quantity);

		if (quantity == 1){
			$button.attr("disabled","disabled")
		} else {
			$button.siblings(".minus").attr("disabled",false)
        }
        $(".add-to-cart").attr({'value':quantity})
    });

	$(".minus_update, .plus_update").click(function(e){
		var $button = $(this);
		var $quantity = $button.siblings(".new_quantity");
		var quantity = parseInt($quantity.text());

		if ($button.hasClass("minus_update")){
			quantity--;
		} else {
			quantity++;
		}
			$quantity.text(quantity);

		if (quantity == 0){
			$button.attr("disabled","disabled")
		} else {
			$button.siblings(".minus_update").attr("disabled",false)
        }
        $(".adjust-cart").attr({'value':quantity})
	});
})
