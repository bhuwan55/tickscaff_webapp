jQuery(function ($) {
  // $('.table').removeClass('table-dark');

  //   $(".sidebar-dropdown > a").click(function() {
  // $(".sidebar-submenu,.sidebar-dropdown-inner").slideUp(200);
  // if (
  //   $(this)
  //     .parent()
  //     .hasClass("active")
  // ) {
  //   $(".sidebar-dropdown").removeClass("active");
  //   $(this)
  //     .parent()
  //     .removeClass("active");
  // } else {
  //   $(".sidebar-dropdown").removeClass("active");
  //   $(this)
  //     .next(".sidebar-submenu,.sidebar-dropdown-inner")
  //     .slideDown(200);
  //   $(this)
  //     .parent()
  //     .addClass("active");
  // }
  // $('.deleteuser').click(function(){
  //     console.log('pressed delete');
  //
  //
  //
  //     });

$('.sidebar-submenu-inner').css('display','none');
$('.sidebar-dropdown>a').click(function(){


  $(this).next('.sidebar-submenu').slideToggle(200);

})

$('.sidebar-dropdown.a>a').click(function(){
$(this).parent().next('.sidebar-submenu-inner').slideToggle(200);


})

$('.sidebar-dropdown.b>a').click(function(){
$(this).next('.sidebar-submenu-inner').slideToggle(200);


})



$("#close-sidebar").click(function() {
  $(".page-wrapper").removeClass("toggled");
});
$("#show-sidebar").click(function() {
  $(".page-wrapper").addClass("toggled");
});





  });
$(document).ready(function(){

$("#deliverydate-input-date").datepicker({
    dateFormat: 'dd/mm/yy'
}).on("changeDate", function (e) {
   var dateFormat= 'dd/mm/yy';
   var d=new Date();
   d=e.date;

  $('#deliverydate-input').val(d.toLocaleDateString());
    // console.log(e.date);
    // alert('hi');
});

 // $('.btn-filter').click(function(){
 //        var $panel = $(this).parent().next('.filterable'),
 //        $filters = $panel.find('.filters input'),
 //        $tbody = $panel.find('.table tbody');
 //        if ($filters.prop('disabled') == true) {
 //            $filters.prop('disabled', false);
 //            $filters.first().focus();
 //        } else {
 //            $filters.val('').prop('disabled', true);
 //            $tbody.find('.no-result').remove();
 //            $tbody.find('tr').show();
 //        }
 //    });

 $('[data-search]').on('keyup', function() {
  var searchVal = $(this).val();
  var filterItems = $('[data-filter-item]');

  if ( searchVal != '' ) {
    filterItems.addClass('hidden');
    $('[data-filter-item][data-filter-name*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
  } else {
    filterItems.removeClass('hidden');
  }
});

//var order_num = 1;
//var count_products =1;

//end for product price button
order_num = 1;

calculateSum();


$('#cashdelivery').on('change',function(){

        //var optionValue = $(this).val();
        //var optionText = $('#dropdownList option[value="'+optionValue+'"]').text();
      var value= $("#cashdelivery option:selected" ).text();
      // alert(value);

      if(value=='Non-COD'){

       $('#collected_price').val('0').prop('readonly', true);
      }
      else{
        $('#collected_price').val('').prop('readonly', false);
        calculateSum();
      }

});

$(".price").on("keydown keyup click", function() {
  // alert($('#cashdelivery').val());
  if ($('#cashdelivery').val() == "cod") {
    calculateSum();
  }
});
count = 0;
balance_amount = parseInt('{{ order.cash_receivable }}')-parseInt('{{ order.service_charge}}');

$('#balance_amount').text(balance_amount);
$('#balance_amount').prop('id', 'balance_amount'+count);

order_num = 1;

function calculateSum() {
  var total_price  = 0;
  //iterate through each textboxes and add the values
  $(".price").each(function() {
  //add only if the value is number
    if (!isNaN(this.value) && this.value.length != 0) {
      total_price += parseFloat(this.value);
      $(this).css("background-color", "#FEFFB0");
    }
    else if (this.value.length != 0){
        $(this).css("background-color", "#f28585");
    }
  });

  $("#collected_price").val(total_price.toFixed(2));
}

function calculateSum1() {
  var total_price  = 0;
  //iterate through each textboxes and add the values
  $(".price").each(function() {
  //add only if the value is number
    if (!isNaN(this.value) && this.value.length != 0) {
      total_price += parseFloat(this.value);
      $(this).css("background-color", "#FEFFB0");
    }
    else if (this.value.length != 0){
        $(this).css("background-color", "#f28585");
    }
  });

  $("#edit-collected_price").val(total_price.toFixed(2));
}

$('.deleterow').click(function(){

  $(this).parents('.added').remove();
    calculateSum();
})

$('.addprice').click(function() {
  var $last_div = $('div[id^="info"]:last');
  var $div = $('div[id^="info"]:first');
//  var product_num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  var count_products = parseInt($('#count-products1').val());
  var product_num = (count_products+order_num);
    var $clone = $div.clone().prop('id', 'info'+(product_num+100) ).addClass('added');
    $clone.find('#product').prop('name','product_'+order_num+'_'+product_num).val("").end();
//  $clone.find('#product').prop('id','product_'+order_num+'_'+product_num);
    $clone.find('#price').prop('name','price_'+order_num+'_'+product_num).val("").end().append(`<button type="button" class="btn btn-primary deleteuser deleterow"><i class="far fa-trash-alt"></i></button>`);
//  $clone.find('#price').prop('id','price_'+order_num+'_'+product_num);

    $last_div.after($clone);
    count_products++;

    $('#count-products'+order_num).val(count_products);
    $('.price').on("keyup focus",function(){
//          alert(count_products);


      $(".price").on("keydown keyup click", function() {
        calculateSum();
      });
    });

     $('.deleterow').click(function(){

       $(this).parents('.added').remove();
         calculateSum();
     })


});

$('.editaddprice').click(function() {
  var $div = $('div[id^="edit-info"]:last').addClass('added');
//  var product_num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  var count_products = parseInt($('#edit-count-products1').val());
  var product_num = (count_products+order_num);
    // alert(product_num);
    var $clone = $div.clone().prop('id', 'edit-info'+(product_num+100) );
    $clone.find('#edit-product').prop('name','edit-product_'+order_num+'_'+product_num).val("").end();
//  $clone.find('#product').prop('id','product_'+order_num+'_'+product_num);
    $clone.find('#edit-price').prop('name','edit-price_'+order_num+'_'+product_num).val("").end().append(`<button type="button" class="btn btn-primary deleteuser deleterow"><i class="far fa-trash-alt"></i></button>`);
//  $clone.find('#price').prop('id','price_'+order_num+'_'+product_num);

    $div.after($clone);
    count_products++;

    $('#edit-count-products'+order_num).val(count_products);
    $('.price').on("keyup focus",function(){
      $(".price").on("keydown keyup click", function() {
        calculateSum1();
      });
    });
    $('.deleterow').click(function(){

      $(this).parents('.added').remove();
        calculateSum1();
    })
});

$('#add-new-order-btn').click(function() {
  // alert('add entry');
  var $div = $('div[id^="data"]:last');
  var num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  var product_num =order_num-num;

  var $clone = $div.clone(true,true).prop('id', 'data'+num );
  $clone.find('#order_id').prop('name','order_id'+num);
  $clone.find('#receiver_name').prop('name','receiver_name'+num);
  $clone.find('#entry_date').prop('name','entry_date'+num);
  $clone.find('#receiver_street_address').prop('name','receiver_street_address'+num);
  $clone.find('#receiver_contactone').prop('name','receiver_contactone'+num);
  $clone.find('#receiver_contacttwo').prop('name','receiver_contacttwo'+num);
  $clone.find('#product').prop('name','product_'+order_num+'_'+product_num);
  $clone.find('#price').prop('name','price_'+order_num+'_'+product_num);
  $clone.find('#weight').prop('name','weight'+num);
  $clone.find('#collected_price').prop('name','collected_price'+num);

  $clone.find('#service_charge').prop('name','service_charge'+num);
  $clone.find('#estimated_delivery_date').prop('name','estimated_delivery_date'+num);
  $clone.find('#remarks').prop('name','remarks'+num);

  $clone.find('#count-products'+(order_num)).prop('id','count-products'+(order_num+1));

  $clone.find('#product_price_container'+order_num).remove();
  $clone.find('#product_price_div'+(order_num)).prop('id','product_price_div'+(order_num+1));
  $clone.find('.addprice').prop('id','btn-add-product'+(order_num+1));

  $div.after($clone);

    $("<div>",{
        id: "product_price_container"+(order_num+1),
//        class: 'row form-group',
    }).appendTo('#product_price_div'+(order_num+1));
//    alert(order_num);
    $("<div>",{
        id: "info"+((10*(order_num+1))+"1"),
    }).appendTo('#product_price_container'+(order_num+1));

    $("<div>",{
        class: 'row form-group',
    }).addClass('product_price').appendTo('#info'+((10*(order_num+1))+"1"));

    $("<div>",{
        class: 'col col-md-6 product_col',
    }).appendTo('.row.form-group.product_price').append('<label>Product</label><input type="text" class="form-control" id="product" name="product_'+(order_num+1)+'_1" placeholder="product">');

    $("<div>",{
        class: 'col col-md-6 price_col',
    }).appendTo('.row.form-group.product_price').append('<label>Price</label><input type="text" class="form-control" id="product" name="price_'+(order_num+1)+'_1" placeholder="price">');;
$("<div>",{
class:'col col-md-12',


}).append('<button class="btn btn-primary addbtn">Add</button>');
//    $("<div>",{
//        class: 'col col-md-6',
//    }).appendTo(after('#info'+((10*(order_num+1))+"1")));

//    $("<label>",{
//        id: "product_price_container",
//        text: "Product",
//    }).appendTo('#info'+(order_num+(100*(order_num+1))));
//

    order_num++;
    $('#count-orders').val(order_num);
    $('#count-products'+order_num).val(1); //for new order details after order_number increments
 });

  $('.new1').click(function() {
  // alert('add entry');
  var $div = $('div[id^="pickupdata"]:last');
  var num = parseInt( $div.prop("id").match(/\d+/g), 10 ) +1;
  // alert(num);
  var $clone = $div.clone().prop('id', 'pickupdata'+num );
  $clone.find('#pickup_orderId').prop('name','pickup_orderId'+num);
  $clone.find('#pickup_order_location').prop('name','pickup_order_location'+num);

  $div.after($clone);


});



// filter

$(".table-search").on("keyup", function() {
  var value = $(this).val().toLowerCase(),
    tableattr = $(this).attr("data-table-search"),
    tablesearch = $('#' + tableattr).find('tbody tr');

  tablesearch.hide();                           //start with all rows hidden
                  //initiate our stored rowspan with the default of 1

  tablesearch.each(function() {
    var $row = $(this);
    var $firstCell = $row.find("td:nth-child(1)");
    var id = $firstCell.text().toLowerCase();
    if (id.indexOf(value) > -1) {               //if the text is found
      $row.show();         //show this row, and the next (n-1) rows as well
    }

  });

});


var padding_right,
    currentModal,
    my_block;

$(document).on('shown.bs.modal', '.modal', function () {
  padding_right=$("body").css("padding-right"); /* create a variable with padding-right when modal is shown */
});

$(document).on('hidden.bs.modal', '.modal', function () {
  /* This function is triggered when a modal is hidden and... */
  if($('.modal:visible').length)
    $(document.body).addClass('modal-open').css("padding-right", padding_right); /* ...if there are some modal visible, it put on body class "model-open" & padding-right */
  else
    $(document.body).removeAttr("style"); /* ...if not remove only style attribute: having put "data-dismiss="modal on button next and prev modal.js automaticaly remove "modal-open" */
});



         //    $(".tablesearch").on("keyup", function() {
         // // alert('in lookup');
         // var value = $(this).val().toLowerCase(),
         // tableattr = $(this).attr("data-table-search"),
         // tablesearch = $('#' + tableattr).find('tbody tr');

         // tablesearch.hide();                           //start with all rows hidden
         //             //initiate our stored rowspan with the default of 1

         // tablesearch.each(function() {
         // var $row = $(this);
         // var $firstCell = $row.find("td:nth-child(3)");
         // var id = $firstCell.text().toLowerCase();

         // // alert($firstCell.toString());
         // if (id.indexOf(value) > -1) {               //if the text is found
         // $row.show();         //show this row, and the next (n-1) rows as well
         // }

         // });

         // });



         //                $(".table-search-order").on("keyup", function() {
         // // alert('in lookup');
         // var value = $(this).val().toLowerCase(),
         // tableattr = $(this).attr("data-table-search"),
         // tablesearch = $('#' + tableattr).find('tbody tr');

         // tablesearch.hide();                           //start with all rows hidden
         //             //initiate our stored rowspan with the default of 1

         // tablesearch.each(function() {
         // var $row = $(this);

         // var $firstCell = $row.find("td:nth-child(3)");
         // var id = $firstCell.text().toLowerCase();

         // // alert($firstCell.toString());
         // if (id.indexOf(value) > -1) {               //if the text is found
         // $row.show();         //show this row, and the next (n-1) rows as well
         // }

         // });

         // });




});


/*/////////////////// new Js from samana Feb 20 //////////////////////////////*/


var countLocation=1;
    $('.add-location').click(function() {
  // alert('add entry');
  var $div = $('div[id^="location"]:last');
  var num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  // alert(num);
  var $clone = $div.clone().prop('id', 'location'+num );
  $clone.find('#locationprovision_pickup_city').prop('name','locationprovision_pickup_city'+num);
  $clone.find('#locationprovision_delivery_city').prop('name','locationprovision_delivery_city'+num);
  $clone.find('#locationprovision_delivery_charge').prop('name','locationprovision_delivery_charge'+num);
  $div.after($clone).css({

    'border-bottom': '1px solid',
    'padding-bottom': '14px',
        'margin-bottom': '12px'
  });
 countLocation=countLocation+1;
                  $('#count-location').val(countLocation);

});


var countperson=1;
    $('.add-company').click(function() {
  // alert('add entry');
  var $div = $('div[id^="customer"]:last');
  var num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  // alert(num);
  var $clone = $div.clone().prop('id', 'customer'+num );
  $clone.find('#customerprovision_contactperson_name').prop('name','customerprovision_contactperson_name'+num);
  $clone.find('#customerprovision_contactperson_phone').prop('name','customerprovision_contactperson_phone'+num);
  $clone.find('#customerprovision_contactperson_email').prop('name','customerprovision_contactperson_email'+num);
    $clone.find('#customerprovision_contactperson_designation').prop('name','customerprovision_contactperson_designation'+num);
  $div.after($clone).css({

    'border-bottom': '1px solid',
    'padding-bottom': '14px',
        'margin-bottom': '12px'
  });
 countperson=countperson+1;
                  $('#count-person').val(countperson);


});

// edit company may23


var editcountperson=1;
    $('.edit-add-company').click(function() {

  // alert('add entry');
  var $div = $('div[id^="editcustomer"]:last');
  var num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
  // alert(num);
  var $clone = $div.clone().prop('id', 'editcustomer'+num );
  $clone.find('#edit-customerprovision_contactperson_name').prop('name','edit-customerprovision_contactperson_name'+num).val("");
  $clone.find('#edit-customerprovision_contactperson_phone').prop('name','edit-customerprovision_contactperson_phone'+num).val("");
  $clone.find('#edit-customerprovision_contactperson_email').prop('name','edit-customerprovision_contactperson_email'+num).val("");
    $clone.find('#edit-customerprovision_contactperson_designation').prop('name','edit-customerprovision_contactperson_designation'+num).val("");
  $div.after($clone).css({

    'border-bottom': '1px solid',
    'padding-bottom': '14px',
        'margin-bottom': '12px'
  });
        editcountperson=editcountperson+1;
                  $('#edit-count-person').val(editcountperson);


});

//


// ---------------------------------------------------------------------------------------

// for adding multiple weightprovision in same page
// --------------------------------------------------------
// var countweight=1;
//     $('.add-weight').click(function() {
//   // alert('add entry');
//   var $div = $('div[id^="weight"]:last');
//   var num =parseInt($div.prop("id").match(/\d+/g), 10 )+1;
//   // alert(num);
//   var $clone = $div.clone().prop('id', 'weight'+num );
//   $clone.find('#weightprovision_weight').prop('name','weightprovision_weight'+num);
//   $clone.find('#weightprovision_weight').prop('id','weightprovision_weight'+num);

//   $clone.find('#weightprovision_deliverycharge').prop('name','weightprovision_deliverycharge'+num);
//   $clone.find('#weightprovision_deliverycharge').prop('id','weightprovision_deliverycharge'+num);

//   $clone.find('#weightprovision_servicecharge').prop('name','weightprovision_servicecharge'+num);
//   $clone.find('#weightprovision_servicecharge').prop('id','weightprovision_servicecharge'+num);


//   $div.after($clone);
//  countweight=countweight+1;
//                   $('#count-weight').val(countweight);

// });

// -------------------------------------------------------------------------------
/*////////////////////////////////////////////////////////////////*/




$('.viewcomment').css('display','none');
$('.comment').click(function(){

$(this).parents().children('.modal-body').find('.viewcomment').css('display','block');

})



/*////////////////////april-1//////////////////////////////////////////////////////////*/








/*//////////////////modal-close//////////////////////////////*/


$('.closestatus').click(function(){

  $(this).parents('#statuschange').modal('hide');
})

$('.closecomment').click(function(){

  $(this).parents('#deliverycomment').modal('hide');

})

$('.closeorderid').click(function(){

  $(this).parents('#orderprint').modal('hide');
})


/*//////////////////////////////////////////////////////////////*/







/*/////////////////////////////////////////////////////////////////////////////////////*/

/*////////////////////////////////////////////////////////////////////////////////////*/

/*//////////////////////may1///////////////////////////////////////////////////////////////*/
window.onload = function(){
  var tableCont = document.querySelector('.scroller');
  /**
   * scroll handle
   * @param {event} e -- scroll event
   */
  function scrollHandle (e){
    var scrollTop = this.scrollTop;
    this.querySelector('thead').style.transform = 'translateY(' + scrollTop + 'px)';
  }

  tableCont.addEventListener('scroll',scrollHandle)
}
/*////////////////////////////////////////////////////////////////////////////////////*/

// may -06

 $(function () {
$(`input:not('input[type="checkbox"]')`).after(`<span class="error"></span>`);
        $("input").keypress(function (e) {
            var keyCode = e.keyCode || e.which;

            $(this).siblings('span').html("");

            //Regex for Valid Characters i.e. Alphabets and Numbers.
            var regex = /^[A-Za-z0-9 $%.,&/\\-\\():@#*+]+$/;

            //Validate TextBox value against the Regex.
            var isValid = regex.test(String.fromCharCode(keyCode));
            if (!isValid) {
              $(this).after("");
              console.log('invalid');
                $(this).siblings('span').html("Invalid character.");

            }
            return isValid;
        });

    });
