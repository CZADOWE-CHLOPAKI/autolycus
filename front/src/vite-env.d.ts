/// <reference types="vite/client" />
interface ImportMetaEnv {
  readonly VITE_SHOW_CRYING_EMOJIS: boolean
  // more env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}