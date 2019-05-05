window.addEventListener("DOMContentLoaded", function() {
    let boxes = document.querySelectorAll(".room");
    
    Array.from(boxes, function(box) {
	box.addEventListener("click", function() {
	    var state = this.getAttribute('data-state');
	    var room = this.classList[1];
	    var URL = 'http://192.168.0.10:5000/' + room;
	    
	    if (state === "off") {
		this.style.backgroundColor = "#dcb";
		this.setAttribute('data-state', 'on');
	    } else {
		this.style.backgroundColor = "#123";
		this.setAttribute('data-state', 'off');
	    }
	    
	    $.ajax({
		url: URL,
		success: function(result) {
		    console.log(result)
		},
		error: function(error) {
		    console.log('Error ${error}')
		}
	    })
	    
    	});
    });


    // Call to start path animation
    let paths = document.querySelectorAll(".path");
    
    Array.from(paths, function(box) {
	box.addEventListener("click", function() {
	    var URL = 'http://192.168.0.10:5000/path';
	    
	    $.ajax({
		url: URL,
		success: function(result) {
		    console.log(result)
		    check("room");
		},
		error: function(error) {
		    console.log('Error ${error}')
		}
	    })
	    
    	});
    });

    
    // Call to shutdown Pi
    let down = document.querySelectorAll(".shutdown");
    
    Array.from(down, function(box) {
	box.addEventListener("click", function() {
	    var URL = 'http://192.168.0.10:5000/shutdown';
	    
	    $.ajax({
		url: URL,
		success: function(result) {
		    console.log(result)
		},
		error: function(error) {
		    console.log('Error ${error}')
		}
	    })
	    
    	});
    });

});


function check(x) {
    elements = document.getElementsByClassName(x);
    for (var i = 0; i < elements.length; i++) {
	elements[i].style.backgroundColor="#123";
    }
}
