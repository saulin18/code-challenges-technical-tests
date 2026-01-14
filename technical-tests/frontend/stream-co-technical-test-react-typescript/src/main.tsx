import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { BrowserRouter, Routes, Route } from 'react-router'
import Home from './pages/Home.tsx'
import AppLayout from './pages/AppLayout.tsx'
import Movies from './pages/Movies.tsx'
import Series from './pages/Series.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route index path='/' element={<Home />} />
          <Route path='/movies' element={<Movies />} />
          <Route path='/series' element={<Series />} />
        </Route>

      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
