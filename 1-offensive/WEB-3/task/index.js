const express = require("express")
const session = require("express-session")
const passport = require("passport")
const nunjucks = require("nunjucks")

const customStrategy = require("passport-custom").Strategy
const SQLiteStore = require("connect-sqlite3")(session)

const flag = process.env.FLAG || "FLAG{FLAG}"
const port = process.env.PORT || 3000;

const app = express()


nunjucks.configure('views', {
    autoescape: true,
    express: app
});
app.use(express.static('static'))

app.use(session({
    secret: 'secret',
    resave: false,
    saveUninitialized: false,
    store: new SQLiteStore({ db: 'sessions.db', dir: "."})
}))

app.use(passport.initialize())

app.use("/*", (req, res, next) => {
    req.isLocalRequest = req.ip.includes("127.0.0.1")
    next()
})

app.use(passport.authenticate('session'))

passport.deserializeUser((user, cb) => {
    cb(null, user)
})
passport.serializeUser((user, cb) => {
    cb(null, user.username)
})

passport.use('local', new customStrategy((req , cb) => {
    cb(null, { username: req.query.username })
}))

app.get("/auth", passport.authenticate('local', {
    successReturnToOrRedirect: '/',
    failureRedirect: '/error',
    failureMessage: true
}))

app.get("/pollute/:param/:value", (req, res) => {
    var a = {}
    a["__proto__"][req.params.param] = req.params.value
    res.send("Polluted!")
})

app.use("/admin/*", (req, res, next) => {
    if (!req.isLocalRequest) return res.send("You should make request locally")
    next()
})

app.get("/admin/flag", (req, res) => {
    res.send(flag)
})

app.get("/", (req, res) => {
    res.render("index.html", { user: req.user })
})

app.listen(port)
