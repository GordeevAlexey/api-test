import { NavLink, Route, Routes } from 'react-router-dom'
import './App.css'

function Header() {
  return (
    <header className="header">
      <div className="brand">VR-Мозг</div>
      <nav className="top-actions">
        <button className="btn" onClick={() => alert('Создание проекта...')}>Создать</button>
        <button className="btn btn-outline">Выйти</button>
      </nav>
    </header>
  )
}

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="section-title">Навигация</div>
      <nav className="menu">
        <NavLink to="/org-home" className={({ isActive }) => isActive ? 'menu-item active' : 'menu-item'}>
          Главная организации
        </NavLink>
        <NavLink to="/projects" className={({ isActive }) => isActive ? 'menu-item active' : 'menu-item'}>
          Проекты
        </NavLink>
        <NavLink to="/users" className={({ isActive }) => isActive ? 'menu-item active' : 'menu-item'}>
          Пользователи
        </NavLink>
        <NavLink to="/settings" className={({ isActive }) => isActive ? 'menu-item active' : 'menu-item'}>
          Настройки
        </NavLink>
      </nav>
    </aside>
  )
}

function StatCard({ title, value, subtitle }: { title: string; value: string; subtitle?: string }) {
  return (
    <div className="stat-card">
      <div className="stat-title">{title}</div>
      <div className="stat-value">{value}</div>
      {subtitle && <div className="stat-subtitle">{subtitle}</div>}
    </div>
  )
}

function OrgHomePage() {
  return (
    <div className="page org-home">
      <div className="stats-grid">
        <StatCard title="Проекты" value="12" subtitle="Активных: 5" />
        <StatCard title="Пользователи" value="48" subtitle="Онлайн: 9" />
        <StatCard title="Задачи" value="327" subtitle="К сроку: 42" />
        <StatCard title="Сессии VR" value="78" subtitle="Сегодня: 6" />
      </div>

      <div className="content-columns">
        <section className="panel">
          <div className="panel-header">
            <h3>Последние проекты</h3>
            <button className="btn btn-small" onClick={() => alert('Переход к списку проектов')}>Все проекты</button>
          </div>
          <table className="table">
            <thead>
              <tr>
                <th>Название</th>
                <th>Статус</th>
                <th>Участников</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>VR Тренажёр Медик</td>
                <td><span className="badge badge-success">Активен</span></td>
                <td>14</td>
              </tr>
              <tr>
                <td>VR Модуль Безопасность</td>
                <td><span className="badge badge-warning">На паузе</span></td>
                <td>7</td>
              </tr>
              <tr>
                <td>VR Лаборатория</td>
                <td><span className="badge">План</span></td>
                <td>3</td>
              </tr>
            </tbody>
          </table>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h3>События</h3>
            <button className="btn btn-small">Подробнее</button>
          </div>
          <ul className="events">
            <li>
              <div className="event-title">Добавлен новый пользователь</div>
              <div className="event-meta">2 часа назад</div>
            </li>
            <li>
              <div className="event-title">Обновлена сессия VR</div>
              <div className="event-meta">вчера</div>
            </li>
            <li>
              <div className="event-title">Создан проект «Лаборатория»</div>
              <div className="event-meta">2 дня назад</div>
            </li>
          </ul>
        </section>
      </div>
    </div>
  )
}

function Placeholder({ title }: { title: string }) {
  return (
    <div className="page">
      <h2>{title}</h2>
      <p>Скоро здесь появится контент.</p>
    </div>
  )
}

export default function App() {
  return (
    <div className="app-shell">
      <Header />
      <div className="body">
        <Sidebar />
        <main className="main">
          <Routes>
            <Route path="/" element={<OrgHomePage />} />
            <Route path="/org-home" element={<OrgHomePage />} />
            <Route path="/projects" element={<Placeholder title="Проекты" />} />
            <Route path="/users" element={<Placeholder title="Пользователи" />} />
            <Route path="/settings" element={<Placeholder title="Настройки" />} />
          </Routes>
        </main>
      </div>
    </div>
  )
}
