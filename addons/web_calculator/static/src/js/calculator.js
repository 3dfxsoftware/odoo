openerp.web_calculator = function (session) {
    var _t = session.web._t,
       _lt = session.web._lt;

session.web.Calculator = session.web.Widget.extend({
    template: 'web_calculator.Calculator',

   start: function () {
            this.$('button').on('click', this.on_calculator );
            this._super();
        },

    on_calculator: function (event) {
    	var self = this;
        event.stopPropagation();
        window.open("/web_calculator/static/src/calculator/calculator.html","_blank",
"left=800,top=100,height=220,width=185,status=yes,toolbar=no,menubar=no,location=no,resizable=no");

    },
	});

	session.web.UserMenu.include({
        do_update: function(){
            var self = this;
            this._super.apply(this, arguments);
            this.update_promise.then(function() {
                var calculator_button = new session.web.Calculator();
                calculator_button.appendTo(session.webclient.$el.find('.oe_systray'));
            });
        },
    });
};


$(document).ready(function(event) {

    $(document).keydown(function(event) {

        var n = String.fromCharCode(event.charCode);
        var d = event.keyCode;
        if (event.keyCode && event.keyCode != 17 && event.ctrlKey) {
            if (d == 85) {

                event.preventDefault();
                window.open("/web_calculator/static/src/calculator/calculator.html","_blank",
"left=800,top=100,height=220,width=185,status=yes,toolbar=no,menubar=no,location=no,resizable=no");

            }
        }
            
    });    
});



