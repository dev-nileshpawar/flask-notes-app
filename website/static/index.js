console.log("testing");
function deleteNote(noteId) {
    console.log("0-----", noteId)
    fetch("/delete-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ noteId })
    }).then(() => window.location.reload()).catch(e=>{
        console.log(e)
    });
}
