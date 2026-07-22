from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('git push --set-upstream origin EIOoNNUB', 'git push --force', '', 'fatal: The current branch EIOoNNUB has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin EIOoNNUB\\n\\n')"

    def test_diversity_2(self):
        return "('git push --set-upstream origin SDOQkTViyI', 'git push --force', '', 'fatal: The current branch SDOQkTViyI has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin SDOQkTViyI\\n\\n')"

    def test_diversity_3(self):
        return "('git push --set-upstream origin VIyDDgTkhWzor', 'git push --force', '', 'fatal: The current branch VIyDDgTkhWzor has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin VIyDDgTkhWzor\\n\\n')"

    def test_diversity_4(self):
        return "('git push --set-upstream origin MoONIBUkr', 'git push -u', '', 'fatal: The current branch MoONIBUkr has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin MoONIBUkr\\n\\n')"

    def test_diversity_5(self):
        return "('git push --set-upstream origin KMekpbQEGJpLX', 'git push --force', '', 'fatal: The current branch KMekpbQEGJpLX has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin KMekpbQEGJpLX\\n\\n')"

    def test_diversity_6(self):
        return "('git push --set-upstream origin QRcNF', 'git push --force', '', 'fatal: The current branch QRcNF has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin QRcNF\\n\\n')"

    def test_diversity_7(self):
        return "('git push --set-upstream origin JiudSvLS', 'git push --force', '', 'fatal: The current branch JiudSvLS has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin JiudSvLS\\n\\n')"

    def test_diversity_8(self):
        return "('git push --set-upstream origin FjzxdqfXKuO', 'git push -u', '', 'fatal: The current branch FjzxdqfXKuO has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin FjzxdqfXKuO\\n\\n')"

    def test_diversity_9(self):
        return "('git push --set-upstream origin POGHONSDTUk', 'git push -u', '', 'fatal: The current branch POGHONSDTUk has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin POGHONSDTUk\\n\\n')"

    def test_diversity_10(self):
        return "('git push --set-upstream origin Iesnj', 'git push -u', '', 'fatal: The current branch Iesnj has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin Iesnj\\n\\n')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('git push --set-upstream origin kesZUfzTW', 'git push', '', 'fatal: The current branch kesZUfzTW has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin kesZUfzTW\\n\\n')"

    def test_diversity_2(self):
        return "('git push --set-upstream origin sBwSFp', 'git push', '', 'fatal: The current branch sBwSFp has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin sBwSFp\\n\\n')"

    def test_diversity_3(self):
        return "('git push --set-upstream origin CdbvFiEQrUiW --quiet', 'git push --quiet', '', 'fatal: The current branch CdbvFiEQrUiW has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin CdbvFiEQrUiW\\n\\n')"

    def test_diversity_4(self):
        return "('git push --set-upstream origin LXDvnmPZ --quiet', 'git push --quiet', '', 'fatal: The current branch LXDvnmPZ has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin LXDvnmPZ\\n\\n')"

    def test_diversity_5(self):
        return "('git push --set-upstream origin WLavmeLrKvV --quiet', 'git push --quiet', '', 'fatal: The current branch WLavmeLrKvV has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin WLavmeLrKvV\\n\\n')"

    def test_diversity_6(self):
        return "('git push --set-upstream origin UmxUQkgP', 'git push', '', 'fatal: The current branch UmxUQkgP has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin UmxUQkgP\\n\\n')"

    def test_diversity_7(self):
        return "('git push --set-upstream origin Obupu --quiet', 'git push --quiet', '', 'fatal: The current branch Obupu has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin Obupu\\n\\n')"

    def test_diversity_8(self):
        return "('git push --set-upstream origin XbFkhneXjUqBn', 'git push', '', 'fatal: The current branch XbFkhneXjUqBn has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin XbFkhneXjUqBn\\n\\n')"

    def test_diversity_9(self):
        return "('git push --set-upstream origin naqCnhE', 'git push', '', 'fatal: The current branch naqCnhE has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin naqCnhE\\n\\n')"

    def test_diversity_10(self):
        return "('git push --set-upstream origin EAkRpjNf', 'git push --set-upstream origin', '', 'fatal: The current branch EAkRpjNf has no upstream branch.\\nTo push the current branch and set the remote as upstream, use\\n\\n    git push --set-upstream origin EAkRpjNf\\n\\n')"
