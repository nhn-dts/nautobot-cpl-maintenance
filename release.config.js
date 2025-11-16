module.exports = {
  branches: ["main"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/github",
    [
      "@semantic-release/exec",
      {
        prepareCmd: "./bump_version.sh ${nextRelease.version}",
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: ["pyproject.toml"], // Add files that should be committed
        message: "build(release): update to version ${nextRelease.version}",
      },
    ],
  ],
};
