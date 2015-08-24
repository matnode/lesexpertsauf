$('.modifcompetence').on('click', function(){
   
    idcompetence=$(this).attr('competenceid');
   
   var nom = $('.nomcompetence'+idcompetence).text();
   var description =  $('.descripcompetence'+idcompetence).text();
   
   //on ajoute charge les valeurs à modifier dans les champs du formulaire
   $('.modfieldnomcompetence').empty().val(nom);
   $('.modfieldescripcompetence').empty().val(description);
   $('[name="idcompetence"]').empty().val(idcompetence);
  
   $('.thecompetence').addClass('animated bounceOutUp').fadeOut();
   $('.modcompetence').show();
   //si on annule on revient sur la liste des compétences
   $('.rollbackcompetence').on('click', function(){    
     $('.thecompetence').removeClass('animated bounceOutUp').fadeIn(500);
     $('.modcompetence').hide()
     
   });
   
   
});

$('.deletecompetence').on('click', function(){
   
    idcompetence=$(this).attr('competenceid');
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idcompetencetodel"]').empty().val(idcompetence);
  
   $('.thecompetence').addClass('animated bounceOutUp').fadeOut();
   $('.delcompetence').show();
   //si on annule on revient sur la liste des compétences
   $('.rollbackcompetence').on('click', function(){
     $('.thecompetence').removeClass('animated bounceOutUp').fadeIn(500);
     $('.delcompetence').hide()
   });
   
});
