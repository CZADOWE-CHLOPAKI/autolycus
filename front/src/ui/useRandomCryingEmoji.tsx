import { useMemo, useState } from 'react';
import CryingLaughSrc from './assets/crying_laugh.png';

const useRandomCryingEmoji = () => {
  const [showCryingEmoji, setShowCryingEmoji] = useState(false);
  const [cryingEmojiCount, setCryingEmojiCount] = useState(150);
  const randomCryingEmoji = useMemo(
    () => generateRandomCryingEmoji(cryingEmojiCount, !showCryingEmoji),
    [cryingEmojiCount, showCryingEmoji]
  );
  const renderRandomCryingEmoji = () => randomCryingEmoji;

  const toggleEmoji = (newState?: boolean) => {
    if (newState === undefined) {
      setShowCryingEmoji(!showCryingEmoji);
      return;
    }
    setShowCryingEmoji(newState);
  };

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

  return [renderCryingEmojiSlider, renderRandomCryingEmoji, toggleEmoji];
};

export default App;
