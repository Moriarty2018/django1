  function cart_del(cart_id){
        del=confirm('确定要删除吗');
        if(del){
            $.get('/my_cart/delete'+cart_id+'/').done(function(data) {
                if (data.ok == 1) {
                    $('ul').remove('#' + cart_id);
                    total();


                }
            })
        }
  }

  /*function total(){
        total1=0;
        total_count=0;
        $('.col07').each(function () {
            count=$(this).prev().find('input').val();
            price=$(this).prev().prev().text();
            total0=parseFloat(count)*parseFloat(price);
            $(this).text(total0.toFixed(2));
            total1+=total0;
            total_count++;
            $('#total').text(total1.toFixed(2));
            $('.total_count1').text(total_count);
        })


  }*/
  /*function my_account() {
      t_account=0;
      t_count=0;
      $(':checkbox').not('#check_all').each(function () {
          num=$(this).next().next().next().next().text();
          pri= $(this).next().next().next().next().next().filter('.num_show').val();
          t_account1=parseFloat(num)*parseFloat(pri);
          $(this).text(t_account1.toFixed(2));
          if($(this).prop('checked')){
              t_account+=t_account1;
              t_count++;
              $('#total').text(t_account.toFixed(2));
              $('.total_count1').text(t_count);
          }



      })

  }*/
  function total(){
        total1=0;
        total_count=0;
        $('.col07').each(function () {
            count=$(this).prev().find('input').val();
            price=$(this).prev().prev().text();
            total0=parseFloat(count)*parseFloat(price);
            $(this).text(total0.toFixed(2));

            total1+=total0;
            total_count++;
            $('#total').text(total1.toFixed(2));
            $('.total_count1').text(total_count);
        })


  }






    $(function(){
        total();

        $('#check_all').click(function(){
            state=$(this).prop('checked');
            $(':checkbox').not('#check_all').prop('checked',state);
        });
        $(':checkbox').not('#check_all').click(function(){
            if($(this).prop('checked')){
                if($(':checked').length+1==$(':checkbox').length){
                    $('#check_all').prop('checked',true);
                    total();

                }
                else{
                    $('#check_all').prop('checked',false);

                }


            }
            //total();

        })
        $('.add').click(function(){
            txt=$(this).next();
            txt.val(parseFloat(txt.val())+1).blur();
            var new_price = parseFloat(parseFloat(txt.val())+1)*parseFloat($(this).parents('.col05').text());
            $(this).parents('.col07').text(new_price);
            total();

        })
        $('.minus').click(function () {
            txt=$(this).prev();
            if(txt.val()>1){
                txt.val(parseFloat(txt.val())-1).blur();
                var new_price = parseFloat(parseFloat(txt.val())-1)*parseFloat($(this).parents('.col05').text());
                $(this).parents('.col07').text(new_price);
                total();

            }
            else {
                alert('该商品最少为一件');
            }


        })
        $(':checkbox').not('#check_all').each(function(){
            if($(this).prop('checked')==true){
                my_id = $(this).val();
                url = 'cart_id=' + my_id;
            }


        })

    })
    $('.num_show').blur(function(){
        count=$(this).val();
        if(count<=0){
            alert('请输入正确的数量');
            $(this).focus();
            return;
        }
        else if(count>=100){
            alert('数量不能超过100');
            $(this).focus();
            return;
        }




        cart_id=$(this).parents('.cart_list_td').attr('id');
        $.get('/my_cart/edit'+cart_id+'_'+count+'/').done(function(data){
            if(data.ok==0){
                total();

            }
            else{
                $(this).val('1');

            }
        })

    })








