/* Add current copyright year to footer. We don't do it inline because
html-proofer checks HTML before it's fully rendered */
document.querySelectorAll('span.copyright-year').forEach(
    function(element) {
        element.appendChild(document.createTextNode(new Date().getFullYear()));
    }
)

/* Add lightbox to elements with `.lightbox` class */
document.addEventListener('DOMContentLoaded', function() {
    baguetteBox.run('.lightbox', {
        overlayBackgroundColor: 'rgba(0,0,0,0.9)',
        captions: function(element) {
            return element.getElementsByTagName('img')[0].alt;
        }
    });
});

/*!
 * Copy button for code blocks
 * Based on Bootstrap internal docs:
   https://github.com/twbs/bootstrap/blob/master/site/static/docs/4.3/assets/js/src/application.js
 * Copyright 2011-2019 The Bootstrap Authors
 * Copyright 2011-2019 Twitter, Inc.
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 * For details, see https://creativecommons.org/licenses/by/3.0/.
 */
(function(){
    "use strict";

    function makeArray(list){
        return[].slice.call(list)
    }

    // Insert copy to clipboard button before .highlight
    var btnHtml = '<div class="clipboard"><button type="button" class="btn-clipboard" title="Copy to clipboard"><i class="fas fa-copy"></i></button></div>';

    makeArray(document.querySelectorAll('figure.highlight, div.highlight'))
        .forEach(function (element) {
            element.insertAdjacentHTML('beforebegin', btnHtml)
        })

    makeArray(document.querySelectorAll('.btn-clipboard'))
        .forEach(function (btn) {
            var tooltipBtn = new bootstrap.Tooltip(btn)

            btn.addEventListener('mouseleave', function () {
                // Explicitly hide tooltip, since after clicking it remains
                // focused (as it's a button), so tooltip would otherwise
                // remain visible until focus is moved away
                tooltipBtn.hide()
            })
        })

    var clipboard = new ClipboardJS('.btn-clipboard', {
        target: function (trigger) {
            return trigger.parentNode.nextElementSibling
        }
    })
    
    clipboard.on("success",
        function(e){
            $(e.trigger)
                .attr('title', 'Copied!')
                .tooltip('_fixTitle')
                .tooltip('show')
                .attr('title', 'Copy to clipboard')
                .tooltip('_fixTitle')
            e.clearSelection()
        }
    );
    
    clipboard.on("error",
        function(e){
            var modifierKey = /Mac/i.test(navigator.userAgent) ? '\u2318' : 'Ctrl+'
            var fallbackMsg = 'Press ' + modifierKey + 'C to copy'

            $(e.trigger)
                .attr('title', fallbackMsg)
                .tooltip('_fixTitle')
                .tooltip('show')
                .attr('title', 'Copy to clipboard')
                .tooltip('_fixTitle')
        }
    );
})();
