/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    function callBack(resolve, reject){
        setTimeout(resolve, millis)
    }
    return new Promise(callBack);
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */