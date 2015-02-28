var wpmud_qs_tinymce_position = 1;

//multiversion method to insert code into editor
function wpmud_qs_addcode(type) {
	if(type == 'new') {
		var form = jQuery('.media-iframe iframe').contents().find('#quickembed_form').serializeArray();
	}
	else {
		var form = jQuery('#TB_iframeContent').contents().find('#quickembed_form').serializeArray();
	}

	var code;

	if(form[0]['value'] !== 0)
		code = form[0]['value'];

	if(code != '') {
		if(jQuery('#wp-content-wrap', window.parent.document).hasClass('tmce-active')) {
			if(type == 'new') {
				if(window.parent.wpmud_qs_tinymce_position != 0) {
					window.parent.tinyMCE.activeEditor.selection.moveToBookmark(window.parent.tinyMCE.activeEditor.windowManager.insertimagebookmark);
					window.parent.tinyMCE.execCommand("mceInsertContent", false, code);
				}
				jQuery('.media-modal .media-modal-close').click();
			}
			else {
				if(window.parent.wpmud_qs_tinymce_position != 0) {
					window.parent.tinyMCE.activeEditor.selection.moveToBookmark(window.parent.tinyMCE.activeEditor.windowManager.insertimagebookmark);
					window.parent.tinyMCE.execCommand("mceInsertContent", false, code);
				}
				window.parent.tb_remove();
			}
		} else {
			if(type == 'new') {
				window.parent.edInsertContent('',code);
				jQuery('.media-modal .media-modal-close').click();
			}
			else {
				window.parent.edInsertContent('',code);
				window.parent.tb_remove();
			}
		}
	}
}

//New media method only for populating with selected data
function wpmud_qs_manage_selection(type) {
	var done = 0;

	quickembed_select = setInterval(function() {
		if(window && window.parent) {
			if(jQuery('#wp-content-wrap', window.parent.document).hasClass('tmce-active'))
				var selected_content = window.parent.tinyMCE.activeEditor.selection.getContent();
			else
				var selected_content = get_selection();

			if(type == 'new') {
				jQuery('.media-modal-content .media-frame', window.parent.document).addClass('hide-router').removeClass('hide-toolbar');
				jQuery('.media-toolbar-primary a', window.parent.document).removeAttr('disabled');

				if( selected_content != '' && (selected_content.indexOf("[gallery") == -1) ) {
					jQuery('#quickembed_form').find('#quickembed_code').val(selected_content);
				}

				done = 1;
			}
			else {
				var current_quickembed_code = jQuery('#quickembed_form').find('#quickembed_code').val();
				if( selected_content != '' && (selected_content.indexOf("[gallery") == -1) ) {
					jQuery('#quickembed_form').find('#quickembed_code').val(selected_content);

				}

				done = 1;
			}
		}
		if(done == 1) {
			jQuery('#quickembed_form').find('#quickembed_code');
			clearInterval(quickembed_select);
		}
	}, 1);
}

function get_selection() {
	var textComponent = jQuery('#wp-content-editor-container .wp-editor-area', window.parent.document)[0];

	if ( ! textComponent )
		return '';
	
	var selectedText;
	// IE version
	if(window.parent.document.selection != undefined) {
		textComponent.focus();
		var sel = window.parent.document.selection.createRange();
		selectedText = sel.text;
	}
	// Mozilla version
	else
		if (textComponent.selectionStart != undefined) {
			var startPos = textComponent.selectionStart;
			var endPos = textComponent.selectionEnd;
			selectedText = textComponent.value.substring(startPos, endPos)
		}

	return selectedText;
}

//Listeners for click: viewing correct window
jQuery(document).ready(function($) {
	var done = 0;

	$('#wp-content-media-buttons .add_media').mousedown(function() {
		var media_link = $('#wp-content-media-buttons .add_media').attr('href');
		if($('#wp-content-wrap').hasClass('tmce-active')) {
			var selected_content = tinyMCE.activeEditor.selection.getContent();
			wpmud_qs_tinymce_position = tinyMCE.activeEditor.windowManager.insertimagebookmark;
		}
		else
			var selected_content = get_selection();

		if(media_link == '#') {
			if(typeof wp.media != 'undefined') {
				wp.media.view.Menu.prototype.on('ready',function(){

					if( selected_content != '' && (selected_content.indexOf("[gallery") == -1 && done == 0) ) {
						var quickembed_menu_link = $('.media-frame-menu .media-menu').find('a:contains("Insert Embed Code")');
						quickembed_menu_link.click();

						done = 1
					}
				});
			}
		}
		else {
			if( selected_content != '' && (selected_content.indexOf("[gallery") == -1) ) {
				var tb_link_array = media_link.split('&');
				tb_link_array.splice(1, 0, 'tab=quickembed');
				tb_link = tb_link_array.join('&');

				tb_show('', tb_link);
				return false;
			}
		}

	});

});