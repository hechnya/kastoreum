null(function(t){function i(t){return"undefined"==typeof t.which?!0:"number"==typeof t.which&&t.which>0?!t.ctrlKey&&!t.metaKey&&!t.altKey&&8!=t.which&&9!=t.which:!1}t.expr[":"].notmdproc=function(i){return t(i).data("mdproc")?!1:!0},t.material={options:{input:!0,ripples:!0,checkbox:!0,togglebutton:!0,radio:!0,arrive:!0,autofill:!1,withRipples:[".btn:not(.btn-link)",".card-image",".navbar a:not(.withoutripple)",".dropdown-menu a",".nav-tabs a:not(.withoutripple)",".withripple"].join(","),inputElements:"input.form-control, textarea.form-control, select.form-control",checkboxElements:".checkbox > label > input[type=checkbox]",togglebuttonElements:".togglebutton > label > input[type=checkbox]",radioElements:".radio > label > input[type=radio]"},checkbox:function(i){t(i?i:this.options.checkboxElements).filter(":notmdproc").data("mdproc",!0).after("<span class=checkbox-material><span class=check></span></span>")},togglebutton:function(i){t(i?i:this.options.togglebuttonElements).filter(":notmdproc").data("mdproc",!0).after("<span class=toggle></span>")},radio:function(i){t(i?i:this.options.radioElements).filter(":notmdproc").data("mdproc",!0).after("<span class=circle></span><span class=check></span>")},input:function(n){t(n?n:this.options.inputElements).filter(":notmdproc").data("mdproc",!0).each(function(){var i=t(this);if(t(this).attr("data-hint")||i.hasClass("floating-label")){if(i.wrap("<div class=form-control-wrapper></div>"),i.after("<span class=material-input></span>"),i.hasClass("floating-label")){var n=i.attr("placeholder");i.attr("placeholder",null).removeClass("floating-label"),i.after("<div class=floating-label>"+n+"</div>")}if(i.attr("data-hint")&&i.after("<div class=hint>"+i.attr("data-hint")+"</div>"),(null===i.val()||"undefined"==i.val()||""===i.val())&&i.addClass("empty"),i.parent().next().is("[type=file]")){i.parent().addClass("fileinput");var e=i.parent().next().detach();i.after(e)}}}),t(document).on("change",".checkbox input[type=checkbox]",function(){t(this).blur()}).on("keydown paste",".form-control",function(n){i(n)&&t(this).removeClass("empty")}).on("keyup change",".form-control",function(){var i=t(this);""===i.val()&&"undefined"!=typeof i[0].checkValidity&&i[0].checkValidity()?i.addClass("empty"):i.removeClass("empty")}).on("focus",".form-control-wrapper.fileinput",function(){t(this).find("input").addClass("focus")}).on("blur",".form-control-wrapper.fileinput",function(){t(this).find("input").removeClass("focus")}).on("change",".form-control-wrapper.fileinput [type=file]",function(){var i="";t.each(t(this)[0].files,function(t,n){i+=n.name+", "}),i=i.substring(0,i.length-2),i?t(this).prev().removeClass("empty"):t(this).prev().addClass("empty"),t(this).prev().val(i)})},ripples:function(i){t(i?i:this.options.withRipples).ripples()},autofill:function(){var i=setInterval(function(){t("input[type!=checkbox]").each(function(){t(this).val()&&t(this).val()!==t(this).attr("value")&&t(this).trigger("change")})},100);setTimeout(function(){clearInterval(i)},1e4);var n;t(document).on("focus","input",function(){var i=t(this).parents("form").find("input").not("[type=file]");n=setInterval(function(){i.each(function(){t(this).val()!==t(this).attr("value")&&t(this).trigger("change")})},100)}).on("blur","input",function(){clearInterval(n)})},init:function(){t.fn.ripples&&this.options.ripples&&this.ripples(),this.options.input&&this.input(),this.options.checkbox&&this.checkbox(),this.options.togglebutton&&this.togglebutton(),this.options.radio&&this.radio(),this.options.autofill&&this.autofill(),document.arrive&&this.options.arrive&&(t.fn.ripples&&this.options.ripples&&t(document).arrive(this.options.withRipples,function(){t.material.ripples(t(this))}),this.options.input&&t(document).arrive(this.options.inputElements,function(){t.material.input(t(this))}),this.options.checkbox&&t(document).arrive(this.options.checkboxElements,function(){t.material.checkbox(t(this))}),this.options.radio&&t(document).arrive(this.options.radioElements,function(){t.material.radio(t(this))}),this.options.togglebutton&&t(document).arrive(this.options.togglebuttonElements,function(){t.material.togglebutton(t(this))}))}}})(jQuery);