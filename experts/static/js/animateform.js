        
        $('.update_whoiam').on('click', function(){
            $('.modwhoiam').show();
            $('.update_animwhoiam').addClass('animated bounceOutUp').fadeOut();
            
           $('.rollbackwhoiam').on('click', function(){
                
                $('.modwhoiam').hide();
                $('.update_animwhoiam').removeClass('animated bounceOutUp').fadeIn();
            
           });
            
        }); 
        
        
         $('.update_mycords').on('click', function(){
           
             $('.update_mycords').each(function(index){
                $(this).addClass('animated bounceOutUp').fadeOut();
             });
              $('.modmycord').show();
       
          });
        
        
