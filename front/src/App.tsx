import {FC, useMemo, useRef, useState} from 'react';
import CryingLaughSrc from './assets/crying_laugh.png';
import RedditSettings from './RedditSettings';
import WielkiButon from './ui/WielkiButon';
import videosrc from './assets/youtube_short_2.webm';

const generateRandomCryingEmoji = (count: number, hidden: boolean) => {
  return (
    <div
      className="w-0 h-0 overflow-hidden pointer-events-none"
      hidden={hidden}
    >
      {Array.from(Array(count).keys()).map((e, index) => {
        const width = `${Math.floor(Math.random() * 50)}px`;
        return (
          <img
            key={index}
            className="absolute w-10 animate-spin-slow"
            style={{
              top: `${Math.floor(Math.random() * 100)}vh`,
              left: `${Math.floor(Math.random() * 100)}vw`,
              width,
            }}
            src={CryingLaughSrc}
          />
        );
      })}
    </div>
  );
};

function App() {
  const [showCryingEmoji, setShowCryingEmoji] = useState(false);
  const [cryingEmojiCount, setCryingEmojiCount] = useState(150);
  const randomCryingEmoji = useMemo(
    () => generateRandomCryingEmoji(cryingEmojiCount, !showCryingEmoji),
    [cryingEmojiCount, showCryingEmoji]
  );

  const videoSrc = useRef(null);

  const renderCryingEmojiSlider = () => (
    <div className={`w-80 ${!showCryingEmoji ? 'hidden' : 'visible'}`}>
      <input
        type="range"
        value={cryingEmojiCount}
        onChange={(event) => {
          const newCryingEmojiCount = parseInt(event.target.value);
          if (isNaN(newCryingEmojiCount)) return;

          setCryingEmojiCount(newCryingEmojiCount);
        }}
        min={0}
        max={100}
        step={1}
        className="w-full"
      />
    </div>
  );

  const generateVideo = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/videos/create?subreddit=dankmemes", {method: 'POST'})
    const blob = await res.blob();
    const temp = URL.createObjectURL(blob);
    // videoSrc.current.load();
    console.log("res", videoSrc.current, temp)
    display(blob)
  }

  function display( videoFile ) {

    // Preconditions:
    if( !( videoFile instanceof Blob ) ) throw new Error( '`videoFile` must be a Blob or File object.' ); // The `File` prototype extends the `Blob` prototype, so `instanceof Blob` works for both.
    if( !( videoSrc.current instanceof HTMLVideoElement ) ) throw new Error( '`videoEl` must be a <video> element.' );

    //

    const newObjectUrl = URL.createObjectURL( videoFile );

    // URLs created by `URL.createObjectURL` always use the `blob:` URI scheme: https://w3c.github.io/FileAPI/#dfn-createObjectURL
    const oldObjectUrl = videoSrc.current.currentSrc;
    if( oldObjectUrl && oldObjectUrl.startsWith('blob:') ) {
      // It is very important to revoke the previous ObjectURL to prevent memory leaks. Un-set the `src` first.
      // See https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL

      videoSrc.current.src = ''; // <-- Un-set the src property *before* revoking the object URL.
      URL.revokeObjectURL( oldObjectUrl );
    }

    // Then set the new URL:
    videoSrc.current.src = newObjectUrl;
    videoSrc.current.src

    // And load it:
    videoSrc.current.load(); // https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/load

  }



  return (
    <div>
      <video controls autoPlay={true} src={videosrc} height={'500'}>
        {/*<source src={videosrc} type={"video/mp4"} height="500px"/>*/}
      </video>
    </div>
  );
}

export default App;
