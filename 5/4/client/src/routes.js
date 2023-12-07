import Admin from "./pages/Admin";
import Museum from "./pages/Museum";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CardDetails from "./pages/CardDetails"
import About from "./pages/About"

import { ADMIN_URL, MUSEUM_URL, LOGIN_URL, REGISTRATION_URL, CARD_URL, ABOUT_URL } from "./utils/urls";


export const authRoutes = {
    [ADMIN_URL]: Admin,
}

export const publicRoutes = {
    [MUSEUM_URL]: Museum,
    [LOGIN_URL]: Login,
    [ABOUT_URL]: About,
    [REGISTRATION_URL]: Register,
    [CARD_URL]: CardDetails,
}
