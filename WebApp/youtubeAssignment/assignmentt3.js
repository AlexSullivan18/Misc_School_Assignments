
      // 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      // 3. This function creates an <iframe> (and YouTube player) after the API code downloads.
      var player;
      var rect = player.getBoundingClientRect();
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '390',
          width: '640',
          videoId: '6CGyASDjE-U', 
          playerVars: {
            'playsinline': 1
          },
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
      }

      // 4. The API will call this function when the video player is ready.
      function onPlayerReady(event) {
        event.target.playVideo();
        console.log("playing state " + player.getPlayerState())
      }

      // 5. The API calls this function when the player's state changes.
      //    The function indicates that when playing a video (state=1),
      //    the player should play for six seconds and then stop.
      var done = false;
      


      function onPlayerStateChange(event) {
        if ( rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /* or $(window).height() */
          rect.right <= (window.innerWidth || document.documentElement.clientWidth) /* or $(window).width() */) {
          /*
            player.getPlayerState():Number
            Returns the state of the player. Possible values are:
            -1 – unstarted
            YT.PlayerState.ENDED (0)
            YT.PlayerState.PLAYING (1)
            YT.PlayerState.PAUSED (2)
            YT.PlayerState.BUFFERING (3)
            YT.PlayerState.CUED (5)
          */

            if (window.addEventListener) {
              addEventListener('DOMContentLoaded', handler, false);
              addEventListener('load', handler, false);
              addEventListener('scroll', handler, false);
              addEventListener('resize', handler, false);
          } else if (window.attachEvent)  {
              attachEvent('onDOMContentLoaded', handler); // Internet Explorer 9+ :(
              attachEvent('onload', handler);
              attachEvent('onscroll', handler);
              attachEvent('onresize', handler);
          }



          stopVideo
          
          
        }
      }
      function stopVideo() {
        player.stopVideo();
      }

   