/*
	Editorial by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$head = $('head'),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ '361px',   '480px'  ],
			xxsmall:  [ null,      '360px'  ],
			'xlarge-to-max':    '(min-width: 1681px)',
			'small-to-xlarge':  '(min-width: 481px) and (max-width: 1680px)'
		});

	// Stops animations/transitions until the page has ...

		// ... loaded.
			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-preload');
				}, 100);
			});

		// ... stopped resizing.
			var resizeTimeout;

			$window.on('resize', function() {

				// Mark as resizing.
					$body.addClass('is-resizing');

				// Unmark after delay.
					clearTimeout(resizeTimeout);

					resizeTimeout = setTimeout(function() {
						$body.removeClass('is-resizing');
					}, 100);

			});

	// Fixes.

		// Object fit images.
			if (!browser.canUse('object-fit')
			||	browser.name == 'safari')
				$('.image.object').each(function() {

					var $this = $(this),
						$img = $this.children('img');

					// Hide original image.
						$img.css('opacity', '0');

					// Set background.
						$this
							.css('background-image', 'url("' + $img.attr('src') + '")')
							.css('background-size', $img.css('object-fit') ? $img.css('object-fit') : 'cover')
							.css('background-position', $img.css('object-position') ? $img.css('object-position') : 'center');

				});

	// Sidebar.
		var $sidebar = $('#sidebar'),
			$sidebar_inner = $sidebar.children('.inner');

		// Inactive by default on <= large.
			breakpoints.on('<=large', function() {
				$sidebar.addClass('inactive');
			});

			breakpoints.on('>large', function() {
				$sidebar.removeClass('inactive');
			});

		// Hack: Workaround for Chrome/Android scrollbar position bug.
			if (browser.os == 'android'
			&&	browser.name == 'chrome')
				$('<style>#sidebar .inner::-webkit-scrollbar { display: none; }</style>')
					.appendTo($head);

		// Toggle.
			$('<a href="#sidebar" class="toggle">Toggle</a>')
				.appendTo($sidebar)
				.on('click', function(event) {

					// Prevent default.
						event.preventDefault();
						event.stopPropagation();

					// Toggle.
						$sidebar.toggleClass('inactive');

				});

		// Events.

			// Link clicks.
				$sidebar.on('click', 'a', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Vars.
						var $a = $(this),
							href = $a.attr('href'),
							target = $a.attr('target');

					// Prevent default.
						event.preventDefault();
						event.stopPropagation();

					// Check URL.
						if (!href || href == '#' || href == '')
							return;

					// Hide sidebar.
						$sidebar.addClass('inactive');

					// Redirect to href.
						setTimeout(function() {

							if (target == '_blank')
								window.open(href);
							else
								window.location.href = href;

						}, 500);

				});

			// Prevent certain events inside the panel from bubbling.
				$sidebar.on('click touchend touchstart touchmove', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Prevent propagation.
						event.stopPropagation();

				});

			// Hide panel on body click/tap.
				$body.on('click touchend', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Deactivate.
						$sidebar.addClass('inactive');

				});

		// Scroll lock.
		// Note: If you do anything to change the height of the sidebar's content, be sure to
		// trigger 'resize.sidebar-lock' on $window so stuff doesn't get out of sync.

			$window.on('load.sidebar-lock', function() {

				var sh, wh, st;

				// Reset scroll position to 0 if it's 1.
					if ($window.scrollTop() == 1)
						$window.scrollTop(0);

				$window
					.on('scroll.sidebar-lock', function() {

						var x, y;

						// <=large? Bail.
							if (breakpoints.active('<=large')) {

								$sidebar_inner
									.data('locked', 0)
									.css('position', '')
									.css('top', '');

								return;

							}

						// Calculate positions.
							x = Math.max(sh - wh, 0);
							y = Math.max(0, $window.scrollTop() - x);

						// Lock/unlock.
							if ($sidebar_inner.data('locked') == 1) {

								if (y <= 0)
									$sidebar_inner
										.data('locked', 0)
										.css('position', '')
										.css('top', '');
								else
									$sidebar_inner
										.css('top', -1 * x);

							}
							else {

								if (y > 0)
									$sidebar_inner
										.data('locked', 1)
										.css('position', 'fixed')
										.css('top', -1 * x);

							}

					})
					.on('resize.sidebar-lock', function() {

						// Calculate heights.
							wh = $window.height();
							sh = $sidebar_inner.outerHeight() + 30;

						// Trigger scroll.
							$window.trigger('scroll.sidebar-lock');

					})
					.trigger('resize.sidebar-lock');

				});

        // Menu.
        var $menu = $('#menu');

        // Openers.
        $menu.find('.opener').each(function() {

            var $this = $(this);
//            var $subMenu = $this.next('ul');

            $this.on('click', function(event) {

                // Prevent default.
                event.preventDefault();

                // Stop propagation.
                event.stopPropagation();

                // Toggle.
                $this.toggleClass('active');

                // Trigger resize (sidebar lock).
                $window.triggerHandler('resize.sidebar-lock');

            });

        });



//        // Sub-openers.
//        $menu.find('li > ul > li').each(function() {
//
//        var $this = $(this);
//        var $subMenu = $this.children('ul');
//
//        // Hide the submenu by default
//        $subMenu.hide();
//
//        $this.on('click', function(event) {
//
//            // Prevent default.
//            event.preventDefault();
//
//            // Stop propagation.
//            event.stopPropagation();
//
//            // Toggle.
//            $subMenu.slideToggle();
//
//        });
//
//        });


// 팝업창 띄우기
//window.onload = function() {
//    document.getElementById('popup').style.display = 'block';
//    document.getElementById('popup-background').style.display = 'block';
//};

// 팝업창 닫기
//document.getElementById('close-popup').addEventListener('click', function() {
//    document.getElementById('popup').style.display = 'none';
//    document.getElementById('popup-background').style.display = 'none';
//});




// 팝업창 띄우기
window.onload = function() {
    // 로컬 스토리지에 저장된 'popupClosedToday' 값 확인
    if (!localStorage.getItem('popupClosedToday')) {
        document.getElementById('popup').style.display = 'block';
        document.getElementById('popup-background').style.display = 'block';
    }
};

// 팝업창 닫기
document.getElementById('close-popup').addEventListener('click', function() {
    document.getElementById('popup').style.display = 'none';
    document.getElementById('popup-background').style.display = 'none';
});

// 오늘 하루 보지 않기 버튼 클릭 시
document.getElementById('close-today-popup').addEventListener('click', function() {
    // 현재 시간을 기준으로 24시간 후의 만료 시간 설정
    var now = new Date();
    var expiration = new Date(now.getTime() + 24 * 60 * 60 * 1000); // 24시간
    localStorage.setItem('popupClosedToday', expiration);

    // 팝업 닫기
    document.getElementById('popup').style.display = 'none';
    document.getElementById('popup-background').style.display = 'none';
});

// 로컬 스토리지에서 'popupClosedToday' 값 확인 및 만료 처리
function checkPopupExpiration() {
    var storedTime = localStorage.getItem('popupClosedToday');
    if (storedTime) {
        var expirationTime = new Date(storedTime);
        if (new Date() > expirationTime) {
            // 만료 시간이 지나면 로컬 스토리지 값 삭제
            localStorage.removeItem('popupClosedToday');
        }
    }
}

// 페이지 로드 시 만료 시간 확인
checkPopupExpiration();

// 검색 기능 (변경 없음)
//document.getElementById('query').addEventListener('keyup', function(e) {
//    if (e.key === 'Enter') {
//        e.preventDefault();  // 기본 동작 중단
//        return;
//    } else {
//        var searchQuery = e.target.value.toLowerCase();
//        var menuItems = document.querySelectorAll('#menu ul li a, #menu ul li span');
//        menuItems.forEach(function(item) {
//            var itemText = item.textContent.toLowerCase();
//            if (itemText.indexOf(searchQuery) > -1 || item.classList.contains('opener')) {
//                item.style.display = '';
//                var parentItem = item.parentElement;
//                while (parentItem) {
//                    if (parentItem.tagName.toLowerCase() === 'ul' && parentItem.previousElementSibling && parentItem.previousElementSibling.classList.contains('opener')) {
//                        parentItem.previousElementSibling.classList.add('active');
//                        parentItem.previousElementSibling.style.display = '';
//                    }
//                    parentItem = parentItem.parentElement;
//                }
//            } else {
//                if (!item.classList.contains('opener')) {
//                    item.style.display = 'none';
//                }
//            }
//        });
//    }
//});

})(jQuery);



