import { Link } from 'react-router-dom'

export default function App() {
  return (
    <main className="min-h-screen bg-[#F4F1E8] text-[#171916]">
      <h1 className="p-6 text-2xl font-semibold">CaseHop</h1>
      <p className="px-6 text-[#5E655F]">Switch models with confidence.</p>
      <nav className="p-6">
        <Link to="/workspace" className="text-[#171916] underline">
          Open the prepared Case Pack
        </Link>
      </nav>
    </main>
  )
}
