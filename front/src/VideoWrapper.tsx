import { useState } from 'react';

const VideoWrapper = () => {
  const [videoUrl, setVideoUrl] = useState<string>();
  const [isGeneratingVideo, setIsGeneratingVideo] = useState(false);

  const generateVideo = async () => {
    setIsGeneratingVideo(true);
    const res = await fetch(
      'http://localhost:5000/api/videos/create?subreddit=memes',
      { method: 'POST' }
    );
    const blob = await res.blob();

    setVideoUrl(URL.createObjectURL(blob));
    setIsGeneratingVideo(false);
  };

  return (
    <div>
      <button onClick={() => generateVideo()}>zrub film z memow</button>
      {videoUrl && (
        <video
          controls
          autoPlay={true}
          src={videoUrl}
          width={300}
          height={500}
        />
      )}
      {isGeneratingVideo && <div>generuje film....</div>}
    </div>
  );
};

export default VideoWrapper;
