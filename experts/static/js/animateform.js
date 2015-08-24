        
        $('.update_whoiam').on('click', function(){
            $('.modwhoiam').show();
            $('.update_animwhoiam').addClass('animated bounceOutUp').fadeOut();
        }); 
        
        
         $('.update_mycords').on('click', function(){
           
             $('.update_mycords').each(function(index){
                $(this).addClass('animated bounceOutUp').fadeOut();
             });
              $('.modmycord').show();
            
        });
        
