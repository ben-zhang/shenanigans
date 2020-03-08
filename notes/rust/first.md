# Rust

### Beginnings

```rust
fn main() {
	println!("Hello, world!");
}
```

Just like in C++ and C, `main` is special: it is always executed first in each Rust executable.

Similar to C++ and C, Rust is a **compiled language**, meaning we must first run `rustc file.rs` to generate an executable. The executable's default name is `file` with no extension.

People in the Rust community are **Rustaceans**.

### Cargo

Just like Javascript has npm and Python has pip, Rust has Cargo. Cargo acts as both the build system and package manager for Rust. 

Use the following command to create a new project using Cargo:

```shell
$ cargo new hello_cargo
$ cd hello_cargo
```

`cargo new` will instantiate a directory with a `Cargo.toml`, `main.rs`, and a `.gitignore`. You can change which vcs Cargo uses using the `--vcs` flag.

`toml` stands for Tom's OBvious, Minimal Language.

When building. Cargo expects source files to be in `src`. `cargo run` will build and run, while `cargo build` only builds.

`cargo check` will check to see if your code compiles without creating an executable.

