$(document).ready(function() {
    // Carga los datos de la primera página al cargar la página
    cargarDatosTabla(1);
  
    // Maneja el click en los enlaces de paginación
    $('#miTabla').on('click', '.page-link', function(e) {
      e.preventDefault();
      cargarDatosTabla($(this).data('page'));
    });
  
    function cargarDatosTabla(pagina) {
      $.ajax({
        url: '/mi-vista/',
        data: { page: pagina },
        success: function(data) {
          // Actualiza el contenido de la tabla con los datos recibidos
          $('#miTabla tbody').html(data);
        },
        error: function() {
          alert('Ha ocurrido un error al cargar los datos.');
        }
      });
    }
  });