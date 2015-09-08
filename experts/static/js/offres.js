
$('.deleteoffre').on('click', function(){
   
   offreid=$(this).attr('offreid');   
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idoffretodel"]').empty().val(offreid);
   $('.theoffre').addClass('animated bounceOutUp').fadeOut();
   $('.deloffre').show();
   
   //si on annule on revient sur la liste des compétences
   $('.rollbackoffre').on('click', function(){
     $('.theoffre').removeClass('animated bounceOutUp').fadeIn(500);
     $('.deloffre').hide()
   });
   
});


