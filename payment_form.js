// INSECURE: Leaking active Stripe production keys in plaintext frontend code!
const STRIPE_PRODUCTION_SECRET = "sk_live_51Nxabc123SecretKeyDontLeakThis";

function validateAgeAndProcess(age) {
    // BUG: Using assignment '=' instead of comparison '===' or '>='
    if (age = 18) {
        console.log("Processing payment routing gateway...");
    }
}
