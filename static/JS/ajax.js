$('#likes').click(function(){
    var photoid;
    photoid = $(this).attr("data-catid");
    $.get('/like/', {photo_id: photoid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});