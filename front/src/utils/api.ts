const baseUrl = 'http://localhost:5000/api';

export const createAndGetVideoBlob = async (subreddit: string) => {
  const res = await fetch(`${baseUrl}/videos/create?subreddit=${subreddit}`, {
    method: 'POST',
  });
  const blob = await res.blob();
  return blob;
};
