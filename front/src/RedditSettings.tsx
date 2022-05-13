import { useState } from 'react';

type RedditSettingsPropsType = {};

const RedditSettings = ({}: RedditSettingsPropsType) => {
  const [subreddit, setSubreddit] = useState('memes');

  const [imageSrcs, setImageSrcs] = useState<string[]>([
    'https://cdn.vox-cdn.com/thumbor/K0siw3nmr87ZaUnzbzp-Pch4VLo=/0x0:735x500/1820x1213/filters:focal(310x192:426x308):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66727168/image.0.png',
    'https://cdn.vox-cdn.com/thumbor/K0siw3nmr87ZaUnzbzp-Pch4VLo=/0x0:735x500/1820x1213/filters:focal(310x192:426x308):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66727168/image.0.png',
    'https://cdn.vox-cdn.com/thumbor/K0siw3nmr87ZaUnzbzp-Pch4VLo=/0x0:735x500/1820x1213/filters:focal(310x192:426x308):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66727168/image.0.png',
    'https://cdn.vox-cdn.com/thumbor/K0siw3nmr87ZaUnzbzp-Pch4VLo=/0x0:735x500/1820x1213/filters:focal(310x192:426x308):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66727168/image.0.png',
  ]);

  return (
    <div className="flex justify-around max-h-96">
      <div className="max-w-2xl space-y-4">
        <div className="flex space-x-2 ">
          <div>r/</div>
          <input
            className="-skew-x-6 bg-transparent border-4 border-blue-400 focus:outline-none"
            type="text"
            value={subreddit}
            onChange={(e) => setSubreddit(e.target.value)}
          />
        </div>
      </div>

      <div className="max-w-2xl p-4 space-y-2 overflow-y-scroll bg-white shadow-md">
        {imageSrcs.map((imgSrc, idx) => (
          <div className="flex">
            <img
              src={imgSrc}
              key={idx}
              alt="sample img"
              className="w-2/3 h-auto"
            />
            <div className="flex flex-col w-1/3 h-auto space-y-4">
              <button>usuń 💀❗❗❗❗❗❗❗❗</button>
              <button>🔈🔈🔈 posluchaj 🔈🔈🔈</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RedditSettings;
