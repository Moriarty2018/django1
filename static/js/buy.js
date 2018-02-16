$(function () {
    var a = parseFloat($('#price1').val())*parseFloat($('#num1').text());
    $('#zprice').text(a.toFixed(2));
    $('#zprice1 b').text(a.toFixed(2));
    var zongjia = parseFloat($('#price1').val())*parseFloat($('#num1').text())+parseFloat(10);

    $('#shifu b').text(zongjia.toFixed(2));
    $('#order_btn').click(function () {
        if($('#addres').val().length>=10){
            var num = $('#num1').text();
            var gid = $('#good').val();
            var total = parseFloat($('#price1').val())*parseFloat($('#num1').text())+parseFloat(10);

            $.get('/my_cart/buy_order/',{'num':num,'gid':gid,'total':total}).done(function (data) {
                if(data.ok==1){

                    window.location.href='/user/order_1/'
                }
                else {
                    alert('库存不足请修改数量');
                }

            }).fail(function (data) {
                if(data.ok==0){
                    alert('订单提交失败');

                }


                })


        }

        else {
            alert('请设置您的收货地址');
        }


    })

})
