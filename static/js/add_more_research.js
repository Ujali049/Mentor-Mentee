var count=1;
function add_field(){
    count=count+1;

	html='<div class="form-row" id="row'+count+'">\
            <div class="form-holder form-holder-2">\
                <legend>Project 1</legend>\
                <input type="text" class="form-control input-border" id="Project_name'+count+'" name="Project_name'+count+'" placeholder="Project Name" required>\
            </div>\
        </div>\
        <div class="form-row">\
            <div class="form-holder form-holder-2">\
                <input type="text" class="form-control input-border" id="Publication'+count+'" name="Publication'+count+'" placeholder="Publication" required>\
            </div>\
        </div>'
        var form=document.getElementById('product_form')
        form.innerHTML+=html


}