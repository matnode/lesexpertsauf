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


$('.modifmission').on('click', function(){
   
    missionid=$(this).attr('missionid');
   
   //on reccupère le contenu à modifier
   var datedebut= $('.datedebut'+missionid).text();
   var datefin= $('.datefin'+missionid).text();
   var entreprise= $('.entreprise'+missionid).text();
   var fonction= $('.fonction'+missionid).text();
   var titre= $('.titre'+missionid).text();
   var competence= $('.competence'+missionid).text();
   var description= $('.description'+missionid).text();
   
   
   //on charge les valeurs dans le formulaire    
    $('.moddatedebut').empty().val(datedebut);
    $('.moddatefin').empty().val(datefin);
    $('.modentreprise').empty().val(entreprise);
    $('.modfonction').empty().val(fonction);
    $('.modtitre').empty().val(titre);
    $('.modcompetence').empty().val(competence);
    $('.moddescription').empty().val(description);
    $('.idthismission').empty().val(missionid);
   
   $('.themission').addClass('animated bounceOutUp').fadeOut();
   $('.modmission').show();
   //si on annule on revient sur la liste des compétences
  
   $('.rollbackmission').on('click', function(){    
     $('.themission').removeClass('animated bounceOutUp').fadeIn(500);
     $('.modmission').hide()
     
   });   
   
});


$('.deletemission').on('click', function(){
   
    missionid=$(this).attr('missionid');
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idmissiontodel"]').empty().val(missionid);
  
   $('.themission').addClass('animated bounceOutUp').fadeOut();
   $('.delmission').show();
   //si on annule on revient sur la liste des compétences
   $('.rollbackmission').on('click', function(){
     $('.themission').removeClass('animated bounceOutUp').fadeIn(500);
     $('.delmission').hide()
   });
   
});




$('.modiformation').on('click', function(){
   
   formationid=$(this).attr('formationid');
   
   //on reccupère le contenu à modifier
   var datedebut= $('.formationdatedebut'+formationid).text();
   var datefin= $('.formationdatefin'+formationid).text();
   var ecole= $('.formationecole'+formationid).text();
   var titre= $('.formationtitre'+formationid).text();
   var lieu= $('.formationlieu'+formationid).text();
   var diplome= $('.formationdiplome'+formationid).text();
   var description= $('.formationdescription'+formationid).text();
   
   
   //on charge les valeurs dans le formulaire    
    $('.modformationdatedebut').empty().val(datedebut);
    $('.modformationdatefin').empty().val(datefin);
    $('.modformationecole').empty().val(ecole);
    $('.modformationtitre').empty().val(titre);
    $('.modformationlieu').empty().val(lieu);
    $('.modformationdiplome').empty().val(diplome);
    $('.modformationdescription').empty().val(description);
    $('.idthisformation').empty().val(formationid);
   
   $('.theformation').addClass('animated bounceOutUp').fadeOut();
   $('.modformation').show();
   //si on annule on revient sur la liste des compétences
  
   $('.rollbackformation').on('click', function(){    
     $('.theformation').removeClass('animated bounceOutUp').fadeIn(500);
     $('.modformation').hide()
     
   });   
   
});

$('.deleteformation').on('click', function(){
   
    formationid=$(this).attr('formationid');
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idformationtodel"]').empty().val(formationid);
  
   $('.theformation').addClass('animated bounceOutUp').fadeOut();
   $('.delformation').show();
   //si on annule on revient sur la liste des compétences
   $('.rollbackformation').on('click', function(){
     $('.theformation').removeClass('animated bounceOutUp').fadeIn(500);
     $('.delformation').hide()
   });
   
});

$('.modiflangue').on('click', function(){
   
    langueid=$(this).attr('langueid');
   
   var nom = $('.nomlangue'+langueid).text();
   var niveau =  $('.niveaulangue'+langueid).text();
   
   //on ajoute charge les valeurs à modifier dans les champs du formulaire
       $('.modlanguenom').empty().val(nom);
       $('.idthislangue').empty().val(langueid);
  
       $('.thelangue').addClass('animated bounceOutUp').fadeOut();
       $('.modlangue').show();
       
   //si on annule on revient sur la liste des langues
       $('.rollbacklangue').on('click', function(){    
       $('.thelangue').removeClass('animated bounceOutUp').fadeIn(500);
       $('.modlangue').hide();
   });
   
   
});

$('.deletelangue').on('click', function(){
   
   langueid=$(this).attr('langueid');   
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idlanguetodel"]').empty().val(langueid);
   $('.thelangue').addClass('animated bounceOutUp').fadeOut();
   $('.delangue').show();
   
   //si on annule on revient sur la liste des compétences
   $('.rollbacklangue').on('click', function(){
     $('.thelangue').removeClass('animated bounceOutUp').fadeIn(500);
     $('.delangue').hide()
   });
   
});



$('.deleteloisir').on('click', function(){
   
   langueid=$(this).attr('loisirid');   
   
   //on ajoute charge les valeurs à supprimer dans le du formulaire  
   $('[name="idloisirtodel"]').empty().val(langueid);
   $('.theloisir').addClass('animated bounceOutUp').fadeOut();
   $('.deloisir').show();
   
   //si on annule on revient sur la liste des compétences
   $('.rollbackloisir').on('click', function(){
     $('.theloisir').removeClass('animated bounceOutUp').fadeIn(500);
     $('.deloisir').hide()
   });
   
});

$('.modifloisir').on('click', function(){
   
    loisirid=$(this).attr('loisirid');
   
   var nom = $('.nomloisir'+loisirid).text();
   var description =  $('.descriptionloisir'+loisirid).text();
   
   //on ajoute charge les valeurs à modifier dans les champs du formulaire
       $('.modloisirnom').empty().val(nom);
       $('.modloisirdescription').empty().val(description);
       $('.idthisloisir').empty().val(loisirid);
  
       $('.theloisir').addClass('animated bounceOutUp').fadeOut();
       $('.modloisir').show();
       
   //si on annule on revient sur la liste des langues
       $('.rollbackloisir').on('click', function(){    
       $('.theloisir').removeClass('animated bounceOutUp').fadeIn(500);
       $('.modloisir').hide();
   });
   
   
});

