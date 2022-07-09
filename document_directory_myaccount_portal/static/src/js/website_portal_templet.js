odoo.define('ia_au_saas_enterprise.website_portal_templet', function(require) {

$(document).ready(function(){
    console.log('abcd')
    $("#contract").hide();
    $("#essatto").hide();
    
    $(".myInput").change(function myFunction() {
          console.log('abcdZZ')
          var input, filter, table, tr, td, i;
          input = document.getElementById("myInput");
          filter = input.value.toUpperCase();
          table = document.getElementById("directory_table");
          tr = table.getElementsByTagName("tr");
          for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
              if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }
            }       
          }
        });

        var input = document.getElementById("access_portal");
    if (input != null)
    {
          var strUser = input.options[input.selectedIndex].value;
          if(strUser != "portal_user_admin")
        {
            $("#contract").show();
            $("#essatto").show();
        }
        else
        {
            $("#contract").hide();
            $("#essatto").hide();
        }
        if(strUser == "Select Access")
        {
            $("#contract").hide();
            $("#essatto").hide();
        }
        }

    $("#access_portal").change(function myFunction() {
          var input = document.getElementById("access_portal");
          var strUser = input.options[input.selectedIndex].value;
          if(strUser != "portal_user_admin")
        {
            $("#contract").show();
            $("#essatto").show();
        }
        else
        {
            $("#contract").hide();
            $("#essatto").hide();
        }
        if(strUser == "Select Access")
        {
            $("#contract").hide();
            $("#essatto").hide();
        }
        });
    });

}); 
