var numResponse = 0;

$("input[name='has_options']").change(function(e) {
    if (this.value != 0) {
            $('#poll').append(newPollQuestion);
            $('#buttons').html(addButton() + saveButton());
        }
        else {
            numResponse = 0;
            $('#poll').html("");
            $('#buttons').html(saveButton());
        }
    })

$(document).on('click', '#add', function() {
    $('#poll').append(newPollQuestion);
})
    
$(document).on('click', '#save', function() {
    let data = {'id': $('#id').val()};
    for (let item of $('.options')) {
        data[item.value] = 1;
    }
    console.log(data);
    $.post('/save/'+$('#id').val(), data)
        .done(function(data) {
            console.log(data)
            console.log("Success")
        }).fail(function() {
            console.log("Fail")
        })
})

function newPollQuestion() {
    numResponse++;
    return `<div class="row"><div class="left-num">
    <label class="right inline">${numResponse}.</label>
  </div>
  <div class="right-input">
    <input class="options" type="text" placeholder="Provide option description">
  </div></div>`;
}

function addButton() {
    return "<button class='button round' id='add'>+</button>";
}

function saveButton() {
    return "<hr><div class='row'><button id='save' class='button warning round'>Save</button></div>";
}