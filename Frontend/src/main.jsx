import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import System from './System/system.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <System />
  </StrictMode>,
)
