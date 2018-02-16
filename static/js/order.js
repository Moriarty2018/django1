function total(){
        total1=0;
        total_count=0;
        $('.col07').each(function () {
            count=$(this).prev().text();
            price=$(this).prev().prev().text();
            total0=parseFloat(count)*parseFloat(price);
            $(this).text(total0.toFixed(2));
            total1+=total0;
            total_count++;
            total2 = total1 +10
            $('.total_goods_count b').text(total1.toFixed(2));
            $('.total_goods_count em').text(total_count);
            $('.total_pay b').text(total2.toFixed(2));
            $('#total').val(total2.toFixed(2));
        })

  }
$(function(){
    $('#total').hide()
    total();
})

