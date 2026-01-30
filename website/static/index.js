console.log("testing");
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ noteId })
    }).then(res => {
        if (res.ok) location.reload()
    })
}

