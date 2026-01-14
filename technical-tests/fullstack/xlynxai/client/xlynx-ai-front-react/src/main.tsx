import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { BrowserRouter, Route, Routes } from 'react-router'
import App from './App.tsx'
import { QueryClientConfig } from './common/queryclient-config'
import { AuthProvider } from './features/auth/auth-context'
import { AuthPage } from './features/auth/auth-page'
import TasksPage from './features/task/tasks-page.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientConfig>
      <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<App />} />
          <Route path='/auth' element={<AuthPage />} />
          <Route path='/tasks' element={<TasksPage />} />
        </Routes>
      </BrowserRouter>
      </AuthProvider>
    </QueryClientConfig>
  </StrictMode>
)
