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
        $(".add-to-basket-button").attr({'value':quantity})
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
        $(".adjust-basket-form").attr({'value':quantity})
	});
})

$(document).ready(function(){
	$('.slider').slick({
		centerMode: true,
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 1
  })
});
