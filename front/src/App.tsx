import { FC, useMemo, useState } from 'react';
import CryingLaughSrc from './assets/crying_laugh.png';
import RedditSettings from './RedditSettings';
import WielkiButon from './ui/WielkiButon';

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

  return (
    <div>
      <div className="grid w-screen h-screen space-y-32 text-3xl bg-indigo-200 place-content-center">
        <div onMouseOver={() => setShowCryingEmoji(true)}>
          <WielkiButon>
            przycisk gigantyczny wielki ze potezny i mozna wygenerowac filmik
            fajny po prostu a okej
          </WielkiButon>
        </div>
        <RedditSettings />
        {renderCryingEmojiSlider()}
      </div>
      {randomCryingEmoji}
    </div>
  );
}

export default App;
